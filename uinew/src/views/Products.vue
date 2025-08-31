<template>
  <div class="">
    
    <Header/>


    <div
      class="px-6 lg:px-10 py-5 flex flex-col gap-4 items-center justify-center mt-10"
    >
      <div class="container mx-auto max-w-7xl px-4">
        <div class="grid lg:grid-cols-3 gap-10">
          <!-- {{ posts }} -->
          <div v-for="i in posts" :key="i">
            <router-link :to="{ name: 'product', params: { id: i.id }}"
              class="flex flex-col gap-2 text-sm border-[2px] rounded-2xl" 
            >
              <!-- <img
                class="rounded-2xl"
                src="https://media.istockphoto.com/id/1190555610/vector/artificial-intelligence-of-modern-technology-brain-in-laptop.jpg?s=612x612&w=0&k=20&c=SqfO6Lvq2tPISnwlzrdVJArDZKBeTAPaNQU2fuST3Yc="
                alt=""
              /> -->
              <div class="flex items-center justify-center py-20">
                <img width="50" height="50" src="https://img.icons8.com/ios/50/product.png" alt="product"/>
              </div>

              <div class="bg-gray-200 w-[100%] h-[3px]"></div>

              <div class="px-6 pb-5 flex flex-col gap-2"> 
                <h3 class="text-sm font-bold pt-2">{{i.text}}</h3>
                <p class="text-xs">
                  {{i.timestamp}}
                </p>
                {{ i.user_details.username }}
                <p  class="text-xs">Comments: {{ i.comments.length }}</p>
              </div>
            
            </router-link>
          </div>


        </div>

      </div>
    </div>
  </div>
</template>

<script>

import Header from "@/components/Header.vue";
import axios from 'axios';

export default {
  name: "HomeView",

    components: {
      Header
    },

    data() {
        return {
            posts: [],
            loading: false,
            page: 1,
        };
    },
    created() {
        this.loadPosts();
        window.addEventListener('scroll', this.handleScroll);
    },

     methods: {

        // async loadPostsreverse() {
        //     this.loading = true;
        //     try {
        //         const response = await axios.get(`http://127.0.0.1:8000/posts/?page=${this.page}`);
        //         console.log(response.data.results);
        //         this.posts = response.data.results;
        //         this.page--;
        //     } catch (error) {
        //         console.error('Error fetching posts:', error);
        //     }
        //     this.loading = false;
        // },

        async loadPosts() {
            this.loading = true;
            try {
                const response = await axios.get(`http://127.0.0.1:8000/posts/?page=${this.page}`);
                // console.log(response.data.results);
                this.posts.push(...response.data.results);
                this.page++;
            } catch (error) {
                console.error('Error fetching posts:', error);
            }
            this.loading = false;
        },
        handleScroll() {
            console.log(window.innerHeight + window.scrollY >= document.body.offsetHeight - 1);
            if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 1) {
                this.loadPosts();
            }
        }
    },
    beforeDestroy() {
        window.removeEventListener('scroll', this.handleScroll);
    }
};
</script>
