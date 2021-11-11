import React, { Component } from 'react';
import axios from 'axios';


export default class CheckCodon extends Component {
  constructor(props) {
    super(props);
    this.state = {value: '', error: [], result: ""};

    this.handleChange = this.handleChange.bind(this);
    this.checkCodon = this.checkCodon.bind(this);
  }

  handleChange(e) {
    const value = e.target.value;
    this.validationInput(value);
    this.setState({value: e.target.value});
  }

  validationInput(value) {
    let error = []
    var reg = RegExp('^[acgt]+$', 'i')
    if (!Boolean(value.match(reg))){
      error.push('Нуклеотид должен состоять из A, C, G, T')
    }
    if (value.length !== 3)
      error.push('Должно быть 3 нуклеотида')
    this.setState({error:error})
  }

  checkCodon = event =>{
    if (this.state.error.length !== 0)
      alert("Необходимо исправить ошибки")
    else{
      event.preventDefault();
      axios.post(`http://0.0.0.0:8081/api/check_codon/`, { "codon": this.state.value})
        .then(res => {
          if (res.data['result'])
            this.setState({result: "Нуклеотид найден"})
          else
            this.setState({result: "Нуклеотид не найден"})
      });
    }
  }
  render() {
    return(
      <div class="main">
        <h1>Форма поиска кодона в ДНК:</h1>
        <div class="form-container">
          <input 
            type="text" 
            placeholder="Введите кодон" 
            value={this.state.value} 
            onChange={this.handleChange}
          />
          <button onClick={this.checkCodon}>
            Получить ответ
          </button> 
        </div>
        <div>
          {this.state.error.map(item => <p style={{color: 'red'}} key={item}>{item}</p>)}
        </div>
        <div>
            <h2>Результат: </h2>
            <p>{this.state.result}</p>
        </div>       
      </div>
    )
  }

}