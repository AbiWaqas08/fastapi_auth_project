import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="bg-gray-800 text-white px-6 py-4 flex justify-between items-center">
      <Link to="/" className="font-bold text-xl">
        FastAPI Authentication App
      </Link>
      <div className="space-x-4">
        <Link to="/login" className="hover:text-gray-300">
          Login
        </Link>
        <Link to="/signup" className="hover:text-gray-300">
          Sign Up
        </Link>
      </div>
    </nav>
  );
}

export default Navbar;