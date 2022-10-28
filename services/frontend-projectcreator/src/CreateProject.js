import useFetch from "./useFetch";
import { useState } from "react";

const CreateProject = () => {

    const types_url = 'http://localhost:8000/screens/types/'
    const { data: screen_types, error, isPending } = useFetch(types_url)

    const [title, setTitle] = useState('');
    const [desc, setDesc] = useState('');
    const [selectedScreen, setSelectedScreen] = useState('')
    const [screens, setScreens] = useState([]);
    const [isFormPending, setIsFormPending] = useState(false)

    const handleAddScreen = (e) => {

        if (e.target.value !== " ") {

            setScreens((current_screens) => [...current_screens, e.target.value]);
            setSelectedScreen(e.target.value)
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault()

        setIsFormPending(true);

        const create_url = 'http://localhost:8000/project/create/'
        fetch(create_url, { 
            method: 'POST',
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: new URLSearchParams({
                'project_name': title,
                'project_description': desc
            })
        })
        .then(response => {
            if (!response.ok) {
                throw Error('Could not post data')
            }
            return response.json()
        })
        .then(data => {
            const add_screens_url = "http://localhost:8000/project/" + data.id + "/add_screen_comp/"
            fetch(add_screens_url, {
                method: 'POST',
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(screens)
            })
            .then(() => {
                setIsFormPending(false)
            });
        });
    };

    return ( 
        <div className="createproject">
            <h2>Create a New Project</h2>
            <form onSubmit={handleSubmit}>
                <label>Project Title:</label>
                <input
                    type="text"
                    required
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                />
                <label>Project Description:</label>
                <textarea  
                    required
                    value={desc}
                    onChange={(e) => setDesc(e.target.value)}
                ></textarea>
                <label>Add a set of Comps:</label>
                { isPending && <div>Loading...</div>}
                { error && {error} }
                { screen_types && (
                    <select
                        value={selectedScreen}
                        onChange={handleAddScreen}>
                        <option value=" " key="default_value"> </option>
                        {screen_types.ScreenTypes.map((screen_type, index) => (
                            <option value={screen_type} key={index}>{screen_type}</option>
                        ))}
                    </select>
                )}
                { !isFormPending && <button>Add Project</button> }
                { isFormPending && <button disabled>Creating Project...</button>}
                <label>Comps to Add:</label>
                {screens.map((screen, index) => (
                    <li key={index}>{screen}</li>
                ))}
            </form>
        </div>
     );
}
 
export default CreateProject;