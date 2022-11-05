import ListProjects from './ListProjects'
import Navbar from './Navbar';
import CreateProject from './CreateProject';
import ProjectDetails from './ProjectDetails';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';


function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="content">
          <Routes>
            <Route exact path="/projects" element={<ListProjects />} />
            <Route path="/create" element={<CreateProject />} />
            <Route path="/project/:id" element={<ProjectDetails />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
