import { Link } from "react-router-dom";
import { useState } from "react";
import getModifiedTime from "./getModifiedTime";

const ProjectList = ({projects, title}) => {

    const [listProjects, setListProjects] = useState(projects)

    const noProjects = projects.No_Projects;
    let displayProjects = '';
    if (noProjects) {
        displayProjects = <p>No Projects Available</p>
    } else {
        displayProjects = listProjects.map((project) => (
            <div className="project-preview" key={project.id}>
                <Link to={`/project/${project.id}`}>
                    <h2>{project.project_name}</h2>
                    <p>Status: {project.project_status}</p>
                    { getModifiedTime(project.modified_time) }
                </Link>
            </div>
        ))
    }

    return ( 
        <div className="project-list">
            <h2>{title}</h2>
            {displayProjects}
        </div>
     );
}
 
export default ProjectList;