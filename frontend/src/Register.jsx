import React, { useState } from "react";
import { API } from "./api";
import "./styles.css";

export default function Register() {
  const [username, setUser] = useState("");
  const [password, setPass] = useState("");
  const [msg, setMsg] = useState("");

  const register = async () => {
    try {
      const res = await API.post("/register", { username, password });
      setMsg(res.data.message);
    } catch {
      setMsg("Error occurred");
    }
  };

  return (
    <div className="box">
      <h2>Register Button</h2>

      <input
        placeholder="username"
        onChange={(e) => setUser(e.target.value)}
      />

      <input
        placeholder="password"
        type="password"
        onChange={(e) => setPass(e.target.value)}
      />

      <button onClick={register}>Register</button>

      <p className="msg">{msg}</p>
    </div>
  );
}
