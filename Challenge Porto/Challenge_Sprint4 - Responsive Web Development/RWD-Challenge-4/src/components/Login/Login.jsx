import React, { useState } from "react";
import Home from "../../routes/Home";
import "./Login.css";

function Login() {
  const [userData, setUserData] = useState({
    username: "",
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
    if (userData.password.length < 6) {
      validationErrors.password = "A senha deve ser valida";
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
            <h1>Login</h1>
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
                placeholder="Senha"
                type="password"
                name="password"
                value={userData.password}
                onChange={handleChange}
              />
              {errors.password && <p className="error">{errors.password}</p>}
            </div>
            <button className="button-submit" type="submit">
              Logar
            </button>
          </form>
            </div>
        </div>
      )}
    </div>
  );
}

export default Login;