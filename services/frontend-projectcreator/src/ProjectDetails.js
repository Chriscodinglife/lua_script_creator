import useFetch from "./useFetch";
import { useParams } from "react-router-dom";

const ProjectDetails = () => {

    const { id } = useParams();
    const url = 'http://localhost:8000/project/' + id
    const { data: project, error, isPending } = useFetch(url)

    return ( 
        <div className="project-details">
            { isPending && <div>Loading...</div> }
            { error && <div>{ error }</div> }
            { project && (
                <article>
                    <h2>Project Name: { project.project_name }</h2>
                    <h3>Project Description: { project.project_description }</h3>
                    <p>Last Edited: {project.modified_time}</p>
                    <p>Project Status: {project.project_status}</p>
                    <p>id: {project.id}</p>
                    {project.project_comps.Comps.map((comps) => (
                        <div>
                            <p>Comp Name: {comps.comp_name}</p>
                            <p>Height: {comps.width}</p>
                            <p>Width: {comps.height}</p>
                            <p>Types: {comps.types}</p>
                        </div>
                    ))}
                </article>
            )}
        </div>
     );
}
 
export default ProjectDetails;