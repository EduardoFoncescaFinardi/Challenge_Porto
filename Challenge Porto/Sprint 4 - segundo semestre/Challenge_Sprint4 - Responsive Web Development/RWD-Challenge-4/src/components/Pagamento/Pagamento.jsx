import React from 'react'
import './Pagamento.css'
import { Link } from 'react-router-dom'

const Pagamento = () => {
  return (
    <section className='sc-pagamento'>
        <article className='pay'>
            <form action='#' method='POST'>
                <div className='title'>
                    <h3>Cadastro do Cartão</h3>
                </div>
                <label for='nome'>Nome no Cartão:</label>
                <input className='input-text' type="text" id='nome' name='nome' placeholder='Nome do Cartão' required />

                <label for='numero'>Número do Cartão:</label>
                <input type="number" id='numero' name='numero' placeholder='Número do Cartão' required />

                <label for='nome'>Validade:</label>
                <input className='input-text' type="text" id='validade' name='validade' placeholder='Validade' required />

                <label for='cvv'>CVV:</label>
                <input type="number" id='cvv' name='cvv' placeholder='CV' required></input>

                <Link to='/'><input type="submit" value="Cadastrar Cartão"></input></Link>
            </form>
        </article>   
    </section>
  )
}

export default Pagamento