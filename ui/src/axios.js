import axios from "axios";

const instance = axios.create({
  baseURL: "http://ner-python:5555",
  timeout: 3000,
});

export default instance;
