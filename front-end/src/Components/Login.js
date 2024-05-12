import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';
import '../Css/Login.css'

const Login = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      //get data from backend and validate login
      navigate('/dashboard');
    } catch (error) {
      console.error('Error logging in:', error);
      alert('Invalid email or password');
    }
  };


  const [forgotPassword, setForgotPassword] = useState(false);

  const handleForgotPassword = () => {
    setForgotPassword(true);
    // Here you can add your forgot password logic
  };

  return (
   <div>
    <header className='header-nav'>
      <h1>General Magic</h1>
    </header>
    <nav className="login-nav">
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/signup">Sign Up</Link></li>
        </ul>
    </nav>
     <div className="login-container">
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <div className="form-group">
          <label>Email</label>
          <input
            type="email"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Password</label>
          <input
            type="password"
            value={formData.password}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Login</button>
      </form>
      { !forgotPassword && (
        <div className="forgot-password">
          <button onClick={handleForgotPassword}>Forgot Password?</button>
        </div>
      )}
    </div>
   </div>
  );
};

export default Login;
