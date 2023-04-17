<template>
  <div
    v-for="post in APIData"
    :key="post.id"
    class="flex flex-col rounded-lg shadow-lg overflow-hidden"
  >
    <router-link
      :to="{
        name: 'blog',
        params: {
          id: post.id,
          author: post.pub,
          text: post.text,
          pub_date: post.pub_date,
          image: post.image,
          comments: post.comments,
        },
      }"
    ></router-link>
    <div class="card text-center">
      <div class="card-header">{{ post.author }}</div>
      <div class="card-body">
        <h5 class="card-title">Add title</h5>
        {{ post.image }}
        <p class="card-text">
          {{ post.text }}
        </p>
        <a href="#" class="btn btn-primary">Открыть запись</a>
      </div>
      <div class="card-footer text-body-secondary">{{ post.pub_date }}</div>
    </div>
  </div>
</template>

<script>
import { getAPI } from "../axios-api";

export default {
  name: "blog",
  data() {
    return {
      APIData: [],
    };
  },
  created() {
    getAPI
      .get("/api/posts/")
      .then((response) => {
        console.log("Post API has recieved data");
        this.APIData = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>
