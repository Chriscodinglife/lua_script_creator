import useFetch from './useFetch';
import ProjectList from './ProjectList';


const ListProjects = () => {

    const url = 'http://localhost:8000/projects'
    const { data: projects, isPending, error } = useFetch(url)

    return (
        <div className="renderlist">
            <h1>All Projects</h1>
            { error && <div> { error } </div> }
            { isPending && <div>Loading...</div> }
            { projects && <ProjectList projects={projects} /> }
        </div>
    );

}
 
export default ListProjects;