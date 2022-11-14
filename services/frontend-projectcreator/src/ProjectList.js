import { Link } from "react-router-dom";
import { useState } from "react";
import getModifiedTime from "./getModifiedTime";

const ProjectList = ({projects}) => {

    const [listProjects, setListProjects] = useState(projects)

    const noProjects = projects.No_Projects;
    let displayProjects = '';
    if (noProjects) {
        displayProjects = <p>No Projects Available</p>
    } else {
        displayProjects = listProjects.map((project) => (
            <div className="projectbox" key={project.id}>
                <Link className="projectboxdetails" to={`/project/${project.id}`}>
                    <img className="projectboximage" src="/home_page_banner.png" alt="project banner" />
                    <h2 className="project_name">{project.project_name}</h2>
                    { getModifiedTime(project.modified_time) }
                    <p className="project_status">Status: {project.project_status}</p>
                </Link>
            </div>
        ))
    }

    return ( 
        <div className="project-list">
            {displayProjects}
        </div>
     );
}
 
export default ProjectList;