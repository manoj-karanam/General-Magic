import React, { useState } from 'react';
// import axios from 'axios'; 
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';
import '../Css/Login.css';

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
      navigate('/dashboard');
      // // Send a POST request to the login API
      // const response = await axios.post('http://127.0.0.1:8000/api/login/', {
      //   email: formData.email,
      //   password: formData.password
      // });
  
      // // Assuming the response contains a message indicating successful login
      // if (response.data.message === 'Successfully logged in') {
      //   // Redirect to dashboard or another page upon successful login
      //   navigate('/dashboard');
      // } else {
      //   // Handle login failure
      //   alert('Invalid email or password');
      // }
    } catch (error) {
      console.error('Error logging in:', error);
      alert('An error occurred while logging in');
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
          <li><Link to="/">Login</Link></li>
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
            name="email" 
            value={formData.email}
            onChange={handleChange}
            required
            className='login-email'
          />
        </div>
        <div className="form-group">
          <label>Password</label>
          <input
            type="password"
            name="password" 
            value={formData.password}
            onChange={handleChange}
            required
            className='login-pwd'
          />
        </div>
        <button type="submit" className='button-submit'>Login</button>
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
