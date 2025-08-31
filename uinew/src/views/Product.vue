<template>
  <div class="">
    
    <Header/>


         <div class="container mx-auto max-w-7xl px-6 py-6">
            <div>
                <router-link to="/" class="text-xs rounded-full font-Mono bg-black text-white px-4 py-2">Go Back</router-link>
            </div>


                  <div class="flex flex-col lg:flex-row gap-6 py-20">
                <div class="lg:w-[40%] xl:w-[40%]">

                  <div class="flex items-center justify-center py-32 border rounded-xl">
                <img width="50" height="50" src="https://img.icons8.com/ios/50/product.png" alt="product"/>
              </div>

                    <!-- <img width="50" height="50" src="https://img.icons8.com/ios/50/product.png" alt="product"/> -->
                    <!-- <img class="rounded-lg"
                                v-bind:src="apphost+product.image"
                                alt=""> -->
                </div>
                <div class="lg:w-[30%] xl:w-[30%]">
                    <div class="flex flex-col gap-6 lg:px-6">
                        <div>
                            <h1 class="text-2xl font-Mono font-[600]">{{ this.product.text }}</h1>
                          
                        </div>
                        <div class="text-sm font-Mono text-gray-600">
                            <span class="text-black text-sm font-Sans font-[600]">Description:</span>  Demo product for demo 
                        </div>
                         <p class="text-xs">
                  {{product.timestamp}}
                </p>
                <p  class="text-xs" v-if="product.user_details">
                  {{ product.user_details.username }}
                  </p>
                

                <p  class="text-xs" v-if="product.comments">Comments: {{ product.comments.length }}</p>
                    </div>
                </div>
                <div class="lg:w-[30%] xl:w-[30%]">
                    <div class="flex flex-col gap-2 lg:px-6 py-2">
                        <div class="flex flex-col gap-4 border-2 rounded-xl px-6 py-6">
                            <div class="flex flex-row">
                                <p class="text-sm font-Mono w-[50%]">Price :</p>
                                <p class="text-sm font-Mono w-[50%]"> ₹ 100 </p>
                            </div>
                            <div class="flex flex-row">
                                <p class="text-sm font-Mono w-[50%]">Status:</p>
                                <p class="text-sm font-Mono w-[50%]">Available</p>
                              
                            </div>
                          
                            <div class="mt-5">
                            
                                <div>
                                    <button class="bg-black text-white text-sm font-Mono rounded-full px-6 py-2 w-full" @click.prevent="addProduct">Add to Cart</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>


              <div class="py-5 flex flex-col gap-3" v-if="comments">
                <div>
                    <h1 class="font-Mono text-base font-bold pb-5"> Last 3 Reviews</h1>
                </div>

                <div v-if="comments.length == 0" class="text-sm">
                  No reviews
                </div>
                <div class="flex flex-col gap-4"> 
                    <div class="flex flex-col gap-1 border rounded-xl py-3 px-4" v-for="review in comments" :key="review">

                         <p class="text-base font-bold text-gray-800 font-Mono" v-if="review.user_details">{{ review.user_details.username }}</p>
                        <p class="text-sm font-Mono">{{ review.text }}</p>
                         <p class="text-xs font-Mono">{{ review.timestamp }}</p>
                      
                             
              
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
  name: "Product",

    components: {
      Header
    },

    props: ['id'],

    data() {
        return {
          product: "",
          comments: []
        };
    },
    created() {
      this.getProduct();
      this.getComment();
    },

    methods: {

        async getProduct(){
            await axios.get(`http://127.0.0.1:8000/post/${this.id}`)
            .then((response)=>{
                if(response.status == 200){
                    this.product = response.data
                    // console.log(this.product);
                    // this.reviews = response.data.reviews
                }
                else{
                    console.log("Get product Failed.");
                }
            })
            .catch((error)=>{
                console.log(error);
            })
        },

        async getComment(){
            await axios.get(`http://127.0.0.1:8000/comments/${this.id}`)
            .then((response)=>{
                if(response.status == 200){
                    this.comments = response.data
                    // console.log(this.product);
                    // this.reviews = response.data.reviews
                }
                else{
                    console.log("Get comment Failed.");
                }
            })
            .catch((error)=>{
                console.log(error);
            })
        }

    },
};
</script>
