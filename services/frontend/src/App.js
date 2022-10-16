import './App.css';
import { useState } from 'react';
import Form from './Form';

function App() {

  const image_convert_backend = 'http://localhost:8080';
  const lua_backend = 'http://localhost:5000';

  const [allValues, setAllValues] = useState({
    pkgName: '',
    logoData: '',
    productData: '',
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
    e.preventDefault();
    const obsdata = { "package_name": allValues.pkgName,
                      "store_name": allValues.storeName,
                      "support_link": allValues.supportLink,
                      "manual_link": allValues.manual,
                      "logo_image": allValues.logoData,
                      "product_image": allValues.productData };

    let filename = "";

    fetch(lua_backend + "/generate", {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(obsdata),
    })
    .then(response => {
      const disposition = response.headers.get('Content-Disposition');
      filename = disposition.split(/;(.+)/)[1].split(/=(.+)/)[1];
      if (filename.toLowerCase().startsWith("utf-8''"))
            filename = decodeURIComponent(filename.replace("utf-8''", ''));
        else
            filename = filename.replace(/['"]/g, '');
        return response.blob();
    })
    .then(blob => {
        var url = window.URL.createObjectURL(blob); // Create a url path to download
        var a = document.createElement('a'); // Create a link
        a.href = url;
        a.download = filename;
        document.body.appendChild(a); // Append the link to the body
        a.click();
        window.URL.revokeObjectURL(url); // Remove the url path
        a.remove(); // Remove the link
    })
    .catch(error => {
      console.error('Error:', error);
    });

  };


  return (
    <div>
      <h1> OBS Script Creator </h1>
      <h2> Create your obs script below </h2>
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
