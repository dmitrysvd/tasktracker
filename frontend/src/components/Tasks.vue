<template>
  <h1>Task tracker</h1>
  <h3>Списки задач</h3>
  <button class="btn btn-primary" v-for="taskGroup in taskGroups" :key="taskGroup.name" v-on:click="getTasks(taskGroup.id)">
    {{ taskGroup.name }}
  </button>

  <h3>Мои задачи</h3>
  <ul class="list-group">
    <li class="list-group-item list-group-item-action" v-for="task in tasks" :key="task.name">
      <router-link to='/task'>{{ task.name }}</router-link>
    </li>
  </ul>
  <router-view></router-view>
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
      taskGroups: [],
    }
  },
  methods: {
    getTasks(groupId) {
      console.error(groupId);
      axios
        .get("http://localhost:8000/tasks/", {
          params: {group: groupId}
        })
        .then(response => {
          this.tasks = response.data;
        })
        .catch(error => {
          console.error(error);
        })
    },
    getTaskGroups() {
      axios
        .get("http://localhost:8000/task_groups/")
        .then(response => {
          this.taskGroups = response.data;
        })
        .catch(error => {
          console.error(error);
        })
    },
  },
  created() {
    this.getTaskGroups();
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
