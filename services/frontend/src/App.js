import './App.css';
import { useState } from 'react';
import Form from './Form';

function App() {
  const [allValues, setAllValues] = useState({
    logoImage: '',
    productImage: '',
    pkgName: '',
    supportLink: '',
    storeName: '',
    manual: ''
  });

  const handleChange = (e) => {
    setAllValues({...allValues, [e.target.name]: e.target.value});
  };

  const handleSubmit = () => {
    console.log("yes")
  }

  return (
    <div>
      <Form values={allValues} handleChange={handleChange} submit={handleSubmit}></Form>
    </div>
    );
};

export default App;
