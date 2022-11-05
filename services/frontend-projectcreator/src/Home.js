import { Link } from "react-router-dom";

const Home = () => {

    return (
        <div className="home">
            <div className="home-text">
                <h1>One Step Closer On Your Project</h1>
                <p>Projract is a project management tool that helps you to manage your stream design projects in a simple and efficient way.</p>
                <Link className='createbutton' to="/create">Start your new project</Link>
            </div>
            <img src="home_page_banner.png" />
        </div>
    );
}

export default Home;