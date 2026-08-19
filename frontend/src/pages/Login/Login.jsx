import "./Login.css";
import logo from "../../assets/images/logo.jpg";
import cornImage from "../../assets/images/corn.jpg";

function Login() {
    return (
        <div className="login-container">
            <div className="login-left">
                <div className="logo-container">
                    {logo}
                </div>

                <div className="login-card">
                    <h1>Entre na sua conta</h1>
                    <p>
                        Entre com seu e-mail a baixo para acessar sua conta.
                    </p>
                    <form>
                        <div className="form-group">
                            <label htmlFor="email">E-mail</label>
                            <input type="email" id="email" placeholder="Digite seu e-mail" />
                        </div>
                        <div className="password-header">
                            <label htmlFor="password">Senha</label>
                            <a href="#">Esqueceu sua senha?</a>
                        </div>
                        <div className="form-group">
                            <input type="password" id="password" placeholder="Digite sua senha" />
                        </div>
                        <button type="submit">Entrar</button>
                    </form>
                </div>
            </div>
            <div className="login-right">
                <img src={cornImage} alt="Imagem de milho" />
            </div>
        </div>  
    );
}
export default Login;