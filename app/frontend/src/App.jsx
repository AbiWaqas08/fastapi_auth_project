import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Signup from "./pages/Signup";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";

function App() {
  return (
    <Router>
      <div className="min-h-screen flex flex-col bg-gradient-to-b from-blue-50 to-purple-50">
        {/* Navbar only shown on pages other than dashboard */}
        <Routes>
          <Route path="/" element={<Navbar />} />
          <Route path="/signup" element={<Navbar />} />
          <Route path="/login" element={<Navbar />} />
        </Routes>

        <div className="flex-1 flex flex-col items-center justify-center px-4">
          {/* Project Information Card */}
          <div className="w-full max-w-full bg-gradient-to-r from-blue-400 via-purple-400 to-pink-400 text-white rounded-xl shadow-lg p-8 mb-6 text-center">
            <h1 className="text-4xl font-bold mb-3 drop-shadow-lg">
              FastAPI Authentication App
            </h1>
            <p className="text-lg mb-4">
              This project demonstrates a complete authentication system using{" "}
              <span className="font-semibold underline decoration-yellow-300">
                FastAPI
              </span>{" "}
              on the backend and{" "}
              <span className="font-semibold underline decoration-yellow-300">
                React with Vite
              </span>{" "}
              on the frontend.
            </p>
            <p className="text-lg mb-4">
              Features include <span className="font-semibold">Signup</span>,{" "}
              <span className="font-semibold">Login</span>,{" "}
              <span className="font-semibold">JWT-based authentication</span>,{" "}
              <span className="font-semibold">protected routes</span>, and a{" "}
              <span className="font-semibold">full-screen responsive layout</span>{" "}
              using <span className="font-semibold">Tailwind CSS</span>.
            </p>
            <p className="mt-4 text-yellow-100 text-lg">
              Created by <span className="font-bold">Abi Waqas</span>
            </p>
          </div>

          {/* Pages Routes */}
          <Routes>
            <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login />} />
            <Route path="/dashboard" element={<Dashboard />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;