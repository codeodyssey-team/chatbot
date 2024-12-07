const { faker } = require("@faker-js/faker");
const mysql = require("mysql2");

const connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  database: "chatbot",
  password: "Sqlinobj?(no)",
});
 
// Randome user data hello
let getRandomUser = () => {
  return [
    faker.string.uuid(),
    faker.internet.username(),
    faker.internet.email(),
    faker.internet.password(),
  ];
};

// let query = "INSERT INTO users (user_id, username, email, password) VALUES ?";

// let data = [];

// for (let i = 1; i <= 100; i++) {
//   data.push(getRandomUser());
// }

// try {
//   connection.query(query, [data], (err, res) => {
//     if (err) throw err;
//     console.log(res);
//   });
// } catch (err) {
//   console.log(err);
// }

// connection.end();
