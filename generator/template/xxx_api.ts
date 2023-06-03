// todo

// import axios from 'axios';
//
// // Add a request interceptor
// axios.interceptors.request.use(function (config) {
//     // Do something before request is sent
//     return config;
// }, function (error) {
//     // Do something with request error
//     return Promise.reject(error);
// });
// axios.interceptors.response.use(function (response) {
//     // Any status code that lie within the range of 2xx cause this function to trigger
//     // Do something with response data
//     return response;
// }, function (error) {
//     // Any status codes that falls outside the range of 2xx cause this function to trigger
//     // Do something with response error
//     return Promise.reject(error);
// });
//
// // axios.defaults.baseURL = 'http://127.0.0.1:5000/api/v1'; // 设置基本 URL
// axios.defaults.baseURL = 'http://127.0.0.1:5000/'; // 设置基本 URL
//
//
// interface NoteCreate {
//     title?: string | null;
//     content: string;
//     modify_time: string;
// }
//
// interface NoteUpdate {
//     title?: string | null;
//     content: string;
//     modify_time: string;
// }
//
// import { useToast } from "vue-toastification";
// const toast = useToast();
//
//
// interface ResponseData {
//     "success": boolean,
//     "info": string, //业务消息
//     "data": any
// }
// export function create_note(note: NoteCreate){
//     axios.post('/notes/', note).then(res=>{
//         const data:ResponseData = res.data;
//         if(data.success){
//             toast.success(data.info)
//         }else{
//             toast.error(data.info)
//         }
//     })
// }
//
// export async function get_all_notes() {
//     const response = await axios.get('/notes/')
//     const data: ResponseData = response.data
//     if (data.success) {
//         // 处理获取到的所有笔记数据
//         return data.data
//     } else {
//         toast.error(data.info);
//     }
// }
//
// export async function get_note_by_id(note_id: number) {
//     const response = await axios.get(`/notes/${note_id}`)
//     const data: ResponseData = response.data;
//     if (data.success) {
//         // 处理获取到的笔记数据
//         return data.data
//     } else {
//         toast.error(data.info);
//     }
// }
//
// export function update_note(note_id: number, note: NoteUpdate) {
//     axios.put(`/notes/${note_id}`, note).then((res) => {
//         const data: ResponseData = res.data;
//         if (data.success) {
//             toast.success(data.info);
//         } else {
//             toast.error(data.info);
//         }
//     });
// }
//
// export function delete_note(note_id: number) {
//     axios.delete(`/notes/${note_id}`).then((res) => {
//         const data: ResponseData = res.data;
//         if (data.success) {
//             toast.success(data.info);
//         } else {
//             toast.error(data.info);
//         }
//     });
// }