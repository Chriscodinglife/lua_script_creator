import './App.css';
import { useState } from 'react';
import Form from './Form';

function App() {

  const image_convert_backend = 'http://localhost:8080';

  const [allValues, setAllValues] = useState({
    logoData: '',
    productData: '',
    pkgName: '',
    supportLink: '',
    storeName: '',
    manual: ''
  });

  const [logoPath, setLogoPath] = useState('');
  const [productPath, setProductPath] = useState('');

  
  const fetchImageData = (imagePath, setData) => {

    const formData = new FormData();
    formData.append('file', imagePath);
    
    fetch(image_convert_backend + "/convert", {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(result => {
      setAllValues({...allValues, [setData]: result['image']});
    })
    .catch(error => {
      console.error('Error:', error);
    });
  };


  const logoHandler = (e) => {
    setLogoPath(e.target.files[0]);

    fetchImageData(e.target.files[0], 'logoData');

  };


  const productHandler = (e) => {
    setProductPath(e.target.files[0]);

    fetchImageData(e.target.files[0], 'productData');

  };


  const handleChange = (e) => {
    setAllValues({...allValues, [e.target.name]: e.target.value});
  };


  const handleSubmit = (e) => {
    const obsdata = allValues;

  };

  return (
    <div>
      <h1> OBS Script Creator </h1>
      <h2> Create your obs script below</h2>
      <Form 
        values={allValues}
        handleChange={handleChange} 
        submit={handleSubmit} 
        handleLogo={logoHandler} 
        handleProduct={productHandler}></Form>
    </div>
    );
};

export default App;
