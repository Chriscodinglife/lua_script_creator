import { Link } from "react-router-dom";

const Navbar = () => {
    return (
        <nav className="navbar">
            <h1>Stream Project Creator</h1>
            <div className="links">
                <Link to="/">Home</Link>
                <Link to="/create">New Project</Link>
            </div>
        </nav>
    );
}
 
export default Navbar;