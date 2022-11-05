const editedTimeDifference = (time) => {
    const modified_date = new Date(time);
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

export default editedTimeDifference;