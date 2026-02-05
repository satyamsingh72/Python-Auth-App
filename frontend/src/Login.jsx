import React, { useState } from "react";
import { API } from "./api";
import "./styles.css";

export default function Login() {
  const [username, setUser] = useState("");
  const [password, setPass] = useState("");
  const [token, setToken] = useState("");

  const login = async () => {
    try {
      const res = await API.post("/login", { username, password });
      localStorage.setItem("token", res.data.token);
      setToken("Login successful!");
    } catch {
      setToken("Invalid credentials");
    }
  };

  return (
    <div className="box">
      <h2>Login</h2>

      <input
        placeholder="username"
        onChange={(e) => setUser(e.target.value)}
      />

      <input
        placeholder="password"
        type="password"
        onChange={(e) => setPass(e.target.value)}
      />

      <button onClick={login}>Login</button>

      <p className="msg">{token}</p>
    </div>
  );
}