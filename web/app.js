const vm = new Vue({
    el: '#timetable',
    data: {
        date: '',
        timetable: {},
        tasks: [],
        events: [],
        deadline: '',
        subject: '',
        detail: '',
        tags: '',
        event_date: '',
        event_name: '',
        event_tags: '',
    },
    mounted(){
        let today = new Date();
        today.setHours(today.getHours()+9);
        let todayString = today.toISOString().substr(0, 10);
        this.date = todayString;
        this.deadline = todayString;
        this.event_date = todayString;
    },
    watch: {
        date: function(newDate){
            this.getTimetable(newDate);
            this.getTasks(newDate);
            this.getEvents(newDate);
        }
    },
    methods: {
        getTimetable(date) {
            axios.get('/api/timetable/get?date='+date).then(response => {
                console.log(response);
                this.timetable = response.data;
            }).catch(error => {
                console.error(error);
            })
        },
        getTasks(date) {
            let param = {
                params: {
                    first_day: date,
                    last_day: date,
                }
            };
            axios.get('/api/task/get', param).then(response => {
                console.log(response);
                this.tasks = response.data.response;
            }).catch(error => {
                console.error(error);
            })
        },
        getEvents(date) {
            let param = {
                params: {
                    first_day: date,
                    last_day: date,
                }
            };
            axios.get('/api/event/get', param).then(response => {
                console.log(response);
                this.events = response.data.events;
            }).catch(error => {
                console.error(error);
            })
        },
        addTask(){
            let param = {
                'deadline': this.deadline,
                'subject': this.subject,
                'detail': this.detail,
                'tags': []
            };
            axios.post('/api/task/add', param);
        },
        addEvent(){
            let param = {
                'date': this.event_date,
                'name': this.event_name,
                'tags': [],
            };
            axios.post('/api/event/add', param);
        },
    }
})
