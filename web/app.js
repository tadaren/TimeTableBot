const vm = new Vue({
    el: '#timetable',
    data: {
        date: '',
        timetable: {}
        timetable: {},
        tasks: [],
    },
    mounted(){
        let today = new Date();
        let todayString = today.toISOString().substr(0, 10);
        this.date = todayString;
    },
    watch: {
        date: function(newDate){
            this.getTimetable(newDate);
            this.getTasks(newDate);
        }
    },
    methods: {
        getTimetable(date) {
            axios.get('/api/timetable/get?date='+date).then(response => {
                console.log(response);
                this.timetable = response.data;
            }).catch(
            )
            }).catch(error => {
                console.error(error);
            })
        },
        getTasks(date) {
            let param = {
                first_day: date,
                end_day: date,
            };
            axios.get('/api/task/get', param).then(response => {
                console.log(response);
                this.tasks = response.data.response;
            }).catch(error => {
                console.error(error);
            })
        },
        }
    }
})
