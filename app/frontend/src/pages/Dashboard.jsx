import React from "react";
import { useNavigate } from "react-router-dom";

function Dashboard() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <div className="  flex flex-col items-center text-white p-8">
      <div className="bg-white bg-opacity-20 backdrop-blur-lg rounded-2xl p-2 shadow-2xl max-w-xl w-full text-center">
        <h1 className="text-4xl mb-6 drop-shadow-lg font-black text-pink-300">
          Welcome to Dashboard
        </h1>

        <p className="text-lg mb-6 text-purple-500">
          You are successfully logged in!
        </p>

        <button
          onClick={handleLogout}
          className="mt-4 px-6 py-3 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 rounded-lg font-bold text-white hover:from-pink-500 hover:to-blue-500 transition shadow-lg"
        >
          Logout
        </button>
      </div>
    </div>
  );
}

export default Dashboard;