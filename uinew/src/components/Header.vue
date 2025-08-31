<template>
    <div class="sticky top-0 z-50 px-6">

        <div class="container mx-auto max-w-7xl bg-black rounded-full my-5">
            <div class="flex flex-col lg:flex-row lg:items-center justify-between px-10 py-6 gap-4">

                <div class="flex flex-row items-center justify-between w-full">
                    <div class="flex flex-row gap-2 items-center">
                      
                        <router-link to="/" class="text-white text-sm font-bold">Orders</router-link>
                    </div>
                    <div class="flex flex-row items-center gap-3">
                        
                        <a href="/register" class="text-white text-sm">Register</a>

                        <a href="/login" class="text-white text-sm">Login</a>
                       
                    </div>
                </div>

               

            </div>
        </div>


    </div>
</template>

<script>
// import { mapGetters, mapActions } from "vuex"
// import axios from "axios"

export default {
    name: "Header",
}

</script>

<style></style>