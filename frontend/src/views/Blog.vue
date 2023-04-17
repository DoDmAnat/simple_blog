<template>
  <div class="card text-center">
    <div class="card-header">Featured</div>
    <div class="card-body">
      <h5 class="card-title">Special title asf</h5>
      <p class="card-text">
        With supporting text below as a natural lead-in to additional content.
      </p>
      <a href="#" class="btn btn-primary">Go somewhere</a>
    </div>
    <div class="card-footer text-body-secondary">2 days ago</div>
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

<!-- <div
    class="relative bg-gray-50 pt-16 pb-20 px-4 sm:px-6 lg:pt-24 lg:pb-28 lg:px-8"
  >
    <div class="absolute inset-0">
      <div class="bg-white h-1/3 sm:h-2/3" />
    </div>
    <div class="relative max-w-7xl mx-auto">
      <div class="text-center">
        <h2
          class="text-3xl tracking-tight font-extrabold text-gray-900 sm:text-4xl"
        >
          Simple blog
        </h2>
        <p class="mt-3 max-w-2xl mx-auto text-xl text-gray-500 sm:mt-4">
          Просто текст
        </p>
      </div>
      <div
        class="mt-12 max-w-lg mx-auto grid gap-5 lg:grid-cols-3 lg:max-w-none"
      >
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
                author: post.author,
                text: post.text,
                pub_date: post.pub_date,
                image: post.image,
                comments: post.comments,
              },
            }"
          >
            <p>{{ post.author }}</p>
          </router-link>
          {{ post.text }}
        </div>
      </div>
    </div>
  </div> -->
