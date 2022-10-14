import React, { Component } from 'react'
import Form from './Form'

class App extends Component {
    state = {
        characters: [],
    }

    handleSubmit = (character) => {
        this.setState({ characters: [...this.state.characters, character] })
    }
    
    render() {

        const { characters } = this.state

        return (
            <div className="container">
                <Form handleSubmit={this.handleSubmit} />
            </div>
        )
    }
}

export default App