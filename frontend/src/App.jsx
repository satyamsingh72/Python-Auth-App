import Login from "./Login";
import Register from "./Register";

export default function App() {
  return (
    <div style={{ margin: "20px" }}>
      <h1>Auth App</h1>

      <div style={{ display: "flex", gap: "50px" }}>
        <Register />
        <Login />
      </div>
    </div>
  );
}