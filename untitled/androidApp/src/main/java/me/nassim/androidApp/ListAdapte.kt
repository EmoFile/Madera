package me.nassim.androidApp

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.BaseAdapter
import androidx.appcompat.widget.AppCompatTextView

class ListAdapte(val context: Context, val list: ArrayList<President>): BaseAdapter() {
    override fun getCount(): Int {
        return list.size
    }

    override fun getItem(p0: Int): Any {
        return list[p0]
    }

    override fun getItemId(p0: Int): Long {
        return p0.toLong()
    }

    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val view: View = LayoutInflater.from(context).inflate(R.layout.row_layout,parent, false)

        val presidentId = view.findViewById(R.id.president_id) as AppCompatTextView
        val presidentName = view.findViewById(R.id.president_name) as AppCompatTextView
        val presidentPolitic = view.findViewById(R.id.president_politic) as AppCompatTextView
        val presidentTime = view.findViewById(R.id.president_time) as AppCompatTextView

        presidentId.text = list[position].id.toString()
        presidentName.text = list[position].name
        presidentPolitic.text = list[position].politic
        presidentTime.text = list[position].time

        return view
    }
}