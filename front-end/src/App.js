import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './Components/Login';
import Footer from './Components/Footer';
import SignUp from './Components/SignUp';
import Dashboard from './Components/Dashboard';
import UserDetails from './Components/UserDetails';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
        <Route path="/" element={<Login/>} /> 
        <Route path="/signup" element={<SignUp/>} />     
        <Route path="/dashboard" element={<Dashboard/>} />     
        <Route path="/user-details" element={<UserDetails/>} />     
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}


export default App;
