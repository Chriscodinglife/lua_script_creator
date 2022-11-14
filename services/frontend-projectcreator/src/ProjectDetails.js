import useFetch from "./useFetch";
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import getModifiedTime from "./getModifiedTime";

const ProjectDetails = () => {

    const { id } = useParams();
    const url = 'http://localhost:8000/project/' + id
    const { data: project, error, isPending } = useFetch(url)
    const navigate = useNavigate();


    const handleDelete = () => {
        fetch(url + '/delete', {
            method: 'DELETE'
        }).then(() => {
            navigate('/projects');
        })
    };


    const handleDownloadProjectFolder = () => {
        // Download the project folder
        let filename = "";

        const icons = false;
        const download_url = 'http://localhost:5000/download/?project_name=' + project.project_name + '&iinclude_icons=' + icons;

        fetch(download_url, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
        })
        .then(response => {
            if (!response.ok) {
                throw Error('Could not download project folder');
            } else {
                const disposition = response.headers.get('Content-Disposition');
                filename = disposition.split(/;(.+)/)[1].split(/=(.+)/)[1];
                if (filename.toLowerCase().startsWith("utf-8''"))
                    filename = decodeURIComponent(filename.replace("utf-8''", ''));
                else
                    filename = filename.replace(/['"]/g, '');
                return response.blob();
            }
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
    };

    
    const handleDownloadProjectCSV = () => {

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
                    <h1>{ project.project_name }</h1>
                    <div className="project-details-container">
                        <h2 className='project-desc'>About: { project.project_description }</h2>
                        <p className="project-id">id: {project.id}</p>
                        <p className="project-status">Status: {project.project_status}</p>
                        {getModifiedTime(project.modified_time)}
                    </div>
                    {project.project_comps.Comps.map((comps, index) => (
                    <div key={index} className={comps.comp_name}>
                        <h2>{comps.comp_name}s</h2>
                        <div>Dimensions: {comps.width}w & {comps.height}h</div>
                        <div>Types: {comps.types.map((type,index) => (
                            <p key={index}>{type}</p>
                        ))}</div>
                    </div>
                    ))}
                    
                    <div className="actionbuttons">
                        <button onClick={handleDownloadProjectCSV}>Download CSV</button>
                        <button onClick={handleDownloadProjectFolder}>Download Project Folder</button>
                        <button className='delete' onClick={handleDelete}>Delete Project</button>
                    </div>
                </div>
            )}
            
        </div>
        
     );
}
 
export default ProjectDetails;