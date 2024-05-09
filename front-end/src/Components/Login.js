import React, { useState } from 'react';
import './Login.css'

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [forgotPassword, setForgotPassword] = useState(false);

  const handleLogin = (e) => {
    e.preventDefault();
    // Here you can add your login logic
    console.log('Email:', email);
    console.log('Password:', password);
  };

  const handleForgotPassword = () => {
    setForgotPassword(true);
    // Here you can add your forgot password logic
  };

  return (
    <div className="login-container">
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <div className="form-group">
          <label>Email</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label>Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
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
  );
};

export default Login;
