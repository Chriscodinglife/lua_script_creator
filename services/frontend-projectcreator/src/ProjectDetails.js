import useFetch from "./useFetch";
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";

const ProjectDetails = () => {

    const { id } = useParams();
    const url = 'http://localhost:8000/project/' + id
    const { data: project, error, isPending } = useFetch(url)
    const navigate = useNavigate();

    const handleDelete = () => {
        fetch(url + '/delete', {
            method: 'DELETE'
        }).then(() => {
            navigate('/');
        })
    };

    const editedTimeDifference = () => {
        const modified_date = new Date(project.modified_time);
        const now = new Date();

        const seconds = (now.getTime() - modified_date.getTime()) / 1000;
        const hours = Math.floor(seconds / 60 /60);
        const minutes = Math.floor(seconds /60) - (hours * 60);

        if (hours > 1) {
            return (<p className="project-edit">Last edited {hours + ' hours ' + minutes + ' minutes ago'}</p>)
        } else {
            return (<p className="project-edit">Lasted edited {minutes + ' mins ago'}</p>)
        }
    };

    
    const handleDownloadProject = () => {

        let filename = "";

        const download_url = 'http://localhost:8000/project/' + id + '/get_comps_csv/'
        fetch(download_url)
          .then(response => {
            const disposition = response.headers.get('Content-Disposition');
            filename = disposition.split(/;(.+)/)[1].split(/=(.+)/)[1];
            if (filename.toLowerCase().startsWith("utf-8''"))
                  filename = decodeURIComponent(filename.replace("utf-8''", ''));
              else
                  filename = filename.replace(/['"]/g, '');
              return response.blob();
          })
          .then(blob => {
              var url = window.URL.createObjectURL(blob); // Create a url path to download
              var a = document.createElement('a'); // Create a link
              a.href = url;
              a.download = filename;
              document.body.appendChild(a); // Append the link to the body
              a.click();
              window.URL.revokeObjectURL(url); // Remove the url path
              a.remove(); // Remove the link
          })
          .catch(error => {
            console.error('Error:', error);
          });
    }


    return ( 
        <div className="project-details">
            { isPending && <div>Loading...</div> }
            { error && <div>{ error }</div> }
            { project && (
                <div>
                    <div className="project-details-container">
                        <h1>{ project.project_name }</h1>
                        <p className="project-id">id: {project.id}</p>
                        <h2>About: { project.project_description }</h2>
                        <p className="project-status">Status: {project.project_status}</p>
                        {editedTimeDifference()}
                        {project.project_comps.Comps.map((comps, index) => (
                            <div key={index} className="project-screens">
                                <div>Comp Name: {comps.comp_name}</div>
                                <div>Dimensions: {comps.width}w & {comps.height}h</div>
                                <div>Types: {comps.types.map((type,index) => (
                                    <p key={index}>{type}</p>
                                ))}</div>
                            </div>
                        ))}
                    </div>
                </div>
            )}
            <div className="actionbuttons">
                <button onClick={handleDownloadProject}>Download CSV</button>
                <button onClick={handleDelete}>Delete Project</button>
            </div>
        </div>
        
     );
}
 
export default ProjectDetails;