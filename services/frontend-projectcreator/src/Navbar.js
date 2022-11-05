import { Link } from "react-router-dom";

const Navbar = () => {
    return (
        <nav className="navbar">
            <div className="links">
                <a className="logo" href="/">
                    <img src="/projract_logo_small.png" />
                </a>
                <Link className='button' to="/">Home</Link>
                <Link className='button' to="/projects">Projects</Link>
                <Link className="createbutton" to="/create">New Project</Link>
            </div>
        </nav>
    );
}
 
export default Navbar;