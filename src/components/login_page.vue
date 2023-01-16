<template>
    <div>
        <van-button round type="plain" block>Logout</van-button>
    </div>
</template>

<script>
import { Button } from 'vant';

export default {
    name: 'App',
    components: {
        [Button.name]: Button,
    }
}
</script>