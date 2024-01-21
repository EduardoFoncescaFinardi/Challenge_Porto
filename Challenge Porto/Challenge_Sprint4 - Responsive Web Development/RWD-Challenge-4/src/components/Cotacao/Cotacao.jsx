import React, { useEffect } from 'react'
import './Cotacao.css'
import { Link } from 'react-router-dom'

const Cotacao = () => {

    useEffect(() => {

        const [bike, setBike]= useEffect([])

        fetch("http://localhost:8080/bicicleta/")
          .then((resp) => {
            return resp.json();
          })
          .then((resp) => {
            setBike(resp);
            console.log(resp);
          })
          .catch((error) => {
            console.log(error);
          });
      }, []);

  return (
    <div className='ct-container'>
        <article className='bike'>
            <form action='#' method='POST'>
                <div className='title'>
                    <h3>Cadastro da bike</h3>
                </div>
                <label for='nome'>Modelo da bike:</label>
                <input className='input-marca' type="text" id='bike' name='bike' list="faixa" placeholder='Modelo' required />
                <datalist id="faixa">
                    <option value="Caloi">Caloi</option>
                    <option value="Cannondale">Cannondale</option>
                    <option value="Cervélo">Cervélo</option>
                    <option value="Focus">Focus</option>
                    <option value="Giant">Giant</option>
                    <option value="SCOTT">SCOTT</option>
                    <option value="Sense">Sense</option>
                    <option value="Specialized">Specialized</option>
                </datalist>


                <label for='valor'>Valor da bike:</label>
                <input type="number" id='valor' name='valor' placeholder='R$:' required />

                <label for='numero'>Número de Série:</label>
                <input type="number" id='numero' name='numero' placeholder='Série' required />

                <label for='imagens'>Imagens da bike:</label>
                <input type="file" id='imagens' name='imagens' required></input>


                <Link to='/Pagamentos'><input type="submit" value="Cadastrar Bike"></input></Link>
            </form>
        </article>
    </div>
  )
}

export default Cotacao