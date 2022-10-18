export default function Form(props) {

    return (
        <form class="form" onSubmit={props.submit}>
            <div class='pkgfield'>
            <label class='fieldtitle' htmlFor='pkgName'>Package Name</label>
            <input
                type = "text"
                name = "pkgName"
                class = 'inputfield'
                value = {props.values.pkgName}
                onChange = {props.handleChange}></input>
            </div>
            <div class='storefield'>
            <label class='fieldtitle' htmlFor="storeName">Store Name</label>
            <input
                type = "text"
                name = "storeName"
                class = 'inputfield'
                value = {props.values.storeName}
                onChange = {props.handleChange}></input>
            </div>
            <div class='supportfield'>
            <label class='fieldtitle' htmlFor='supportLink'>Support Link</label>
            <input
                type = "text"
                name = "supportLink"
                class = 'inputfield'
                value = {props.values.supportLink}
                onChange = {props.handleChange}></input>
            </div> 
            <div class='manualfield'>
            <label class='fieldtitle' htmlFor="manual">Manual Link</label>
            <input
                type = "text"
                name = "manual"
                class = 'inputfield'
                value = {props.values.manual}
                onChange = {props.handleChange}></input>
            </div>
            <div class='logobutton'>
                <label htmlFor="logoImage">Logo Image</label>
                <input
                    type = "file"
                    name = "logoImage"
                    onChange = {props.handleLogo}></input>
                </div>
            <div class='productbutton'>
            <label htmlFor="productImage">Product Image</label>
            <input
                type = "file"
                name = "productImage"
                onChange = {props.handleProduct}></input>
            </div>
            <button class='downloadbutton' type="submit">Download File</button>
        </form>
    );
}