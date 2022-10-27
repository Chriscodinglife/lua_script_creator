import Home from './Home';
import Navbar from './Navbar';
import CreateProject from './CreateProject';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="content">
          <Routes>
            <Route exact path="/" element={<Home />} />
            <Route path="/create" element={<CreateProject />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
