import React from "react";
import { Link } from "react-router-dom";


const Navbar = () => {
  return (
    <nav className="bg-green-800 text-white px-6 py-4 flex justify-between items-center shadow-md sticky top-0 z-50">
      <div className="text-xl font-bold">
        <Link to="/">
  ⚽ Predict<span className="text-yellow-600 font-semibold">It</span>
</Link>
      </div>
      <div className="space-x-4">
        <Link to="/"className="hover:underline">Home</Link>
        <Link to="/predictions" className="hover:underline">Predictions</Link>
        <Link to="/register" className="hover:underline">Register</Link>
        <Link to="/login" className="hover:underline">Login</Link>
      </div>
    </nav>
  );
};

export default Navbar;