import React from 'react'

import Header from '../components/Header'
import ImageUpload from '../components/ImageUpload'
import IdForm from '../components/IdFishForm'
import Species from '../components/Species'

export default class AppContainer extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      showSpecies: false
    }
    this.handleFormSumbit = this.handleFormSumbit.bind(this)
    this.handleImgUpload = this.handleImgUpload.bind(this)
    this.fetchSpecies = this.fetchSpecies.bind(this)
  }

  fetchSpecies () {
    // axios.get('/go/to/model')
    //      .then(response => response.data)
    //      .then(fish => this.setState({
    //        showSpecies: true,
    //        species: 'Goldfish'
    //      }))
    //      .catch(err => console.log(err))
    this.setState({
      showSpecies: true,
      species: 'Goldfish'
    })
  }

  handleFormSumbit (formState) {
    this.setState({formState}, this.fetchSpecies)
  }

  handleImgUpload (imgState) {
    this.setState({imgState}, () => console.log(this.state))
  }

  render () {
    return (
      <div className='app-container'>
        <Header />
        <ImageUpload handleFormSumbit={this.handleImgUpload} />
        <IdForm handleFormSumbit={this.handleFormSumbit} />
        {
          this.state.showSpecies
          ? <Species species={this.state.species} />
          : null
        }
      </div>
    )
  }
}
