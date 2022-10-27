import { useEffect, useState } from 'react';

const useFetch = (url) => {

     // State of Projects
     const [data, setData] =  useState(null);
     const [isPending, setIsPending] = useState(true)
     const [error, setError] = useState(null)
 
    // Run upon every change of the Dom
    // Get data from the Project server
    useEffect(() => {

        fetch(url)
        .then(response => {
            if (!response.ok) {
                throw Error('Could not fetch data from resource')
            }
            return response.json()
        })
        .then(data => {
            setData(data)
            setIsPending(false);
            setError(null);
        })
        .catch((error) => {
            setIsPending(false);
            setError(error.message);
        });   
    }, [url]);

    return { data, isPending, error };

}

export default useFetch;