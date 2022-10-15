export default function Form(props) {

    return (
        <form onSubmit={props.handleSubmit}>
            <label htmlFor="logoImage">Logo Image</label>
            <input
                type = "file"></input>
            <label htmlFor="productImage">Product Image</label>
            <input
                type = "file"></input>
            <label htmlFor='pkgName'>Package Name</label>
            <input
                type = "text"
                name = "pkgName"
                value = {props.values.pkgName}
                onChange = {props.handleChange}></input>
            <label htmlFor='supportLink'>Support Link</label>
            <input
                type = "text"
                name = "supportLink"
                value = {props.values.supportLink}
                onChange = {props.handleChange}></input>
            <label htmlFor="storeName">Store Name</label>
            <input
                type = "text"
                name = "storeName"
                value = {props.values.storeName}
                onChange = {props.handleChange}></input>
            <label htmlFor="manual">Manual Link</label>
            <input
                type = "text"
                name = "manual"
                value = {props.values.manual}
                onChange = {props.handleChange}></input>
            <button type="submit">Download OBS File</button>
        </form>
    );
}