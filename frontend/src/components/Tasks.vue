<template>
  <h1>Task tracker</h1>
  <h3>{{ msg }}</h3>
  <h3>Мои задачи</h3>
  <li v-for="task in tasks" :key="task.name">
    {{ task.name }}
  </li>
</template>

<script>
import axios from "axios";

export default {
  name: 'Tasks',
  props: {
    msg: String,
  },
  data() {
    return {
      tasks: [],
    }
  },
  methods: {
    getTasks() {
      axios
        .get("http://localhost:8000/tasks/")
        .then(response => {
          this.tasks = response.data;
        })
        .catch(error => {
          console.error(error);
        })
    },
  },
  created() {
    this.getTasks();
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
