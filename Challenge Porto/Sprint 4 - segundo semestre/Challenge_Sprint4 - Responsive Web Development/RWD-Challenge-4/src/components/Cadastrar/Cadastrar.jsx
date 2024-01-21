import React, { useState } from "react";
import Home from "../../routes/Home";
import "./cadastrar.css";

function Cadastrar() {
  const [userData, setUserData] = useState({
    username: "",
    email: "",
    password: "",
  });
  const [errors, setErrors] = useState({});
  const [isRegistered, setIsRegistered] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setUserData({ ...userData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const validationErrors = {};

    if (userData.username.trim() === "") {
      validationErrors.username = "Campo obrigatório";
    }
    if (!userData.email.match(/^\S+@\S+\.\S+$/)) {
      validationErrors.email = "Email inválido";
    }
    if (userData.password.length < 6) {
      validationErrors.password = "A senha deve ter pelo menos 6 caracteres";
    }

    if (Object.keys(validationErrors).length === 0) {
      setIsRegistered(true);
    } else {
      setErrors(validationErrors);
    }
  };

  return (
    <div className="App">
      {isRegistered ? (
        <Home />
      ) : (
        <div className="background-container">
            <div className="cadastro-container">
            <h1>Cadastro</h1>
          <form onSubmit={handleSubmit}>
            <div className="cadastro-input">
              <input
                placeholder="Usuário"
                type="text"
                name="username"
                value={userData.username}
                onChange={handleChange}
              />
              {errors.username && <p className="error">{errors.username}</p>}
            </div>
            <div className="cadastro-input">
              <input
                className="login-input"
                placeholder="E-mail"
                type="email"
                name="email"
                value={userData.email}
                onChange={handleChange}
              />
              {errors.email && <p className="error">{errors.email}</p>}
            </div>
            <div className="cadastro-input">
              <input
                placeholder="Senha"
                type="password"
                name="password"
                value={userData.password}
                onChange={handleChange}
              />
              {errors.password && <p className="error">{errors.password}</p>}
            </div>
            <button className="button-submit" type="submit">
              Cadastrar
            </button>
          </form>
            </div>
        </div>
      )}
    </div>
  );
}

export default Cadastrar;
