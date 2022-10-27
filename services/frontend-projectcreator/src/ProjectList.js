import { Link } from "react-router-dom";

const ProjectList = ({projects, title}) => {

    return ( 
        <div className="project-list">
            <h2>{title}</h2>
            {projects.map((project) => (
                <div className="project-preview" key={project.id}>
                    <Link to={`/project/${project.id}`}>
                        <h2>{project.project_name}</h2>
                        <p>Status: {project.project_status}</p>
                        <p>Edited on: {project.modified_time}</p>
                    </Link>
                </div>
            ))}
        </div>
     );
}
 
export default ProjectList;