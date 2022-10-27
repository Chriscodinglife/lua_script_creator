const ProjectList = ({projects, title}) => {

    return ( 
        <div className="project-list">
            <h2>{title}</h2>
            {projects.map((project) => (
                <div className="project-preview" key={project.id}>
                    <h2>{project.project_name}</h2>
                    <p>Status: {project.project_status}</p>
                    <p>Edited on: {project.modified_time}</p>
                </div>
            ))}
        </div>
     );
}
 
export default ProjectList;