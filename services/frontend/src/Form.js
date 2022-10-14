import React, { Component } from 'react'

class Form extends Component {
    initialState = {
        logo_image: '',
        product_image: '',
        package_name: '',
        support_link: 'https://www.etsy.com/shop/MoreBackgrounds',
        store_name: 'More Backgrounds',
    }

    state = this.initialState

    handleChange = (event) => {
        const { name, value } = event.target

        this.setState({
            [name]: value,
        })
    }

    submitForm = () => {
        this.props.handleSubmit(this.state)
        this.setState(this.initialState)
    }

    render () {
        const { 
            logo_image,
            product_image,
            package_name,
            support_link,
            store_name } = this.state;
    
        return (
            <form>
                <label htmlFor="logo_image">Your Logo Image</label>
                <input
                    type="text"
                    name="logo_image"
                    id="logo_image"
                    value={logo_image}
                    onChange={this.handleChange} />
                <label htmlFor="product_image">Product Image</label>
                <input
                    type="text"
                    name="product_image"
                    id="product_image"
                    value={product_image}
                    onChange={this.handleChange} />
                <label htmlFor='package_name'>Package Name</label>
                <input
                    type="text"
                    name="package_name"
                    id="package_name"
                    value={package_name}
                    onChange={this.handleChange} />
                <label htmlFor='support_link'>Your Store Link</label>
                <input
                    type="text"
                    name="support_link"
                    id="support_link"
                    value={support_link}
                    onChange={this.handleChange} />
                <label htmlFor='store_name'>Your Store Name</label>
                <input
                    type="text"
                    name="store_name"
                    id="store_name"
                    value={store_name}
                    onChange={this.handleChange} />
                <input type="button" value="Submit" onClick={this.submitForm} />
            </form>
        )
    }

}


export default Form;